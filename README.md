# Deep reinforcement learning for optimizing heat pumps.

## Setup Instructions for `boptestgym`

The `boptestgym` environment is used to simulate heat pump optimization scenarios for reinforcement learning tasks. Follow these steps to set up the environment:

### Prerequisites
Ensure you have the following installed on your system:
- **Python** (version 3.8 or higher)
- **Docker** (for running BOPTEST test cases)
- **pip** (Python package manager)
- **git** (to clone the repository)
- A **Unix-based system** (Linux/MacOS recommended; Windows with WSL may also work)

### Installation Steps

1. Clone the Repository

git clone https://github.com/your-username/RL_energy.git
cd RL_energy

2. Install Required Python Packages

Set up a virtual environment (recommended) and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

3. Pull and Run the BOPTEST Docker Image

Download and run the BOPTEST test case Docker container:
docker pull annex42/boptest-bestest-hydronic
docker run -d -p 5000:5000 annex42/boptest-bestest-hydronic

Ensure the container is running by checking Docker’s container list:
docker ps

4. Verify BOPTEST Connection

Confirm that the BOPTEST environment is accessible:
curl http://localhost:5000
You should see a JSON response with BOPTEST API information.

5. Install boptestgym

From the project directory, install the boptestgym package:
pip install -e .

6. Configure Simulation Parameters

Edit the configuration file in `config/boptest_config.yaml` to match your simulation settings, such as:
- Test case (e.g., `bestest_hydronic_heat_pump`)
- Simulation duration and start time
- Reward function parameters

7. Run Your First Simulation

Execute a test script to ensure everything is set up correctly:
python scripts/test_boptestgym.py

Troubleshooting
- Docker connection issues: Ensure Docker is running, and the container is active.
- Port conflicts: Check if port 5000 is already in use. Modify the `-p` option in the `docker run` command if necessary (e.g., `-p 5001:5000`).
- Dependency errors: Ensure all packages in `requirements.txt` are installed without errors.
