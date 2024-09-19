import hudson.Extension;
import hudson.model.AbstractProject;
import hudson.model.Run;
import hudson.model.TaskListener;
import hudson.tasks.Builder;
 import hudson.tasks.BuildStepDescriptor;
import hudson.tasks.BuildStepMonitor;
import hudson.tasks.Notifier;
import hudson.tasks.Publisher;
import jenkins.tasks.SimpleBuildStep;
import org.kohsuke.stapler.DataBoundConstructor;

public class GitLabCICDPlugin extends Notifier {
    private String gitLabUrl;
    private String gitLabToken;
    private String pipelineId;

    @DataBoundConstructor
    public GitLabCICDPlugin(String gitLabUrl, String gitLabToken, String pipelineId) {
        this.gitLabUrl = gitLabUrl;
        this.gitLabToken = gitLabToken;
        this.pipelineId = pipelineId;
    }

    @Override
    public boolean perform(AbstractBuild<?, ?> build, Launcher launcher, BuildListener listener) {
        // Create a GitLab API client
        GitLabApi gitLabApi = new GitLabApi(gitLabUrl, gitLabToken);

        // Trigger the pipeline
        gitLabApi.triggerPipeline(pipelineId);

        return true;
    }

    @Extension
    public static class DescriptorImpl extends BuildStepDescriptor<Publisher> {
        @Override
        public boolean isApplicable(Class<? extends AbstractProject> jobType) {
            return true;
        }

        @Override
        public String getDisplayName() {
            return "GitLab CI/CD Plugin";
        }
    }
}
