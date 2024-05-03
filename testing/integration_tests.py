import unittest
import bank_account

class TestBankAccount(unittest.TestCase):
    def test_deposit_and_withdraw(self):
        account = bank_account.BankAccount()
        account.deposit(100)
        self.assertEqual(account.balance, 100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

if __name__ == '__main__':
    unittest.main()
