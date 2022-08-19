# pp_cmd_generate
Postprocessing command "generate"

Generates signal 

Usage example:
`... | generate name="new_signal_name", type="sinusoidal", frequency=3, amplitude=1, offset=0, fs=100, duration=10`

## Getting started
###  Prerequisites
1. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installing
1. Create virtual environment with post-processing sdk 
```bash
make dev
```
That command  
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates `pp_cmd` directory with links to available post-processing commands
- creates `otl_v1_config.ini` with otl platform address configuration

2. Configure connection to platform in `otl_v1_config.ini`

### Test generate
Use `pp` to test generate command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | generate name="new_signal_name", type="sinusoidal", frequency=3, amplitude=1, offset=0, fs=100, duration=10 
```
