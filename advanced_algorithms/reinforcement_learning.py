import numpy as np
import tensorflow as tf

class DQNAgent:
    def __init__(self, state_dim, action_dim, learning_rate, discount_factor, epsilon, epsilon_decay, epsilon_min, memory_size, batch_size):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.memory_size = memory_size
        self.batch_size = batch_size

        self.memory = np.zeros((self.memory_size, state_dim * 2 + action_dim + 1), dtype=np.float32)
        self.pointer = 0

        self.model = self.create_model()

    def create_model(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(64, input_dim=self.state_dim, activation='relu'))
        model.add(tf.keras.layers.Dense(64, activation='relu'))
        model.add(tf.keras.layers.Dense(self.action_dim, activation='linear'))
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        index = self.pointer % self.memory_size
        self.memory[index] = np.hstack((state, action, reward, next_state, done))
        self.pointer += 1

    def act(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, self.action_dim)
        else:
            q_values = self.model.predict(state.reshape(1, self.state_dim))
            return np.argmax(q_values)

    def replay(self):
        if self.pointer < self.batch_size:
            return
        minibatch = np.random.choice(self.memory_size, size=self.batch_size, replace=False)
        for index in minibatch:
            state, action, reward, next_state, done = self.memory[index]
            target_q = reward
            if not done:
                target_q = reward + self.discount_factor * np.amax(self.model.predict(next_state.reshape(1, self.state_dim)))
            target = self.model.predict(state.reshape(1, self.state_dim))
            target[0][action] = target_q
            self.model.fit(state.reshape(1, self.state_dim), target, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
