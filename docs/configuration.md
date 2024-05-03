# Configuration Guide for UCTR

## Configuring UCTR

UCTR can be configured using a configuration file or environment variables.

### Configuration File

Create a file named `uctr.cfg` in the same directory as the UCTR executable. This file should contain the following format:

`[uctr] log_level = DEBUG database_url = sqlite:///uctr.db`

Replace `DEBUG` with the desired log level (DEBUG, INFO, WARNING, ERROR, or CRITICAL) and `sqlite:///uctr.db` with the desired database URL.

### Environment Variables

UCTR can also be configured using environment variables. The following environment variables are supported:

* `UCTR_LOG_LEVEL`: sets the log level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
* `UCTR_DATABASE_URL`: sets the database URL

For example, to set the log level to DEBUG and the database URL to `sqlite:///uctr.db`, you can run:

`export UCTR_LOG_LEVEL=DEBUG export UCTR_DATABASE_URL=sqlite:///uctr.db`

### Default Configuration

If no configuration file or environment variables are provided, UCTR will use the following default configuration:

`[uctr] log_level = INFO database_url = sqlite:///uctr.db`

## Advanced Configuration Options

For advanced users, UCTR provides additional configuration options that can be used to customize its behavior. These options are documented in the [UCTR Advanced Configuration Guide](advanced-configuration.md).
