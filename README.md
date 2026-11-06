# Round Robin Load Balancer

This project simulates round-robin request distribution across backend servers.
The simulator generates requests, the load balancer selects an available server,
and statistics summarize how requests were distributed.

## Capacity

The simulation creates 10 servers by default. Each server has a capacity of
200 requests, and the load balancer redirects requests to the next server when
a server reaches 80% capacity (160 requests). This allows the default setup to
handle up to 1,600 requests in one simulation run:

```text
10 servers x 160 requests per server = 1,600 requests fixing on 80% of real server capacity 
```

After all servers reach that threshold, the load balancer has no available
server for additional requests, which are reported as "No available server."
This is a per-run request limit in the simulation, not a measure of concurrent
in-flight requests or an actual system crash.

Create and activate a virtual environment from the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

This project uses only the Python standard library, so no additional packages
need to be installed.

Run the full simulation from the project directory:

```bash
python3 main.py
```

Run the tests from the project directory:

```bash
python3 -m unittest discover -s tests -v
```

The `main.py` entry point was vibe coded.