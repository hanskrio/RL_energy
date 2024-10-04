from boptestGymEnv import BoptestGymEnv, NormalizedObservationWrapper, DiscretizedActionWrapper
from stable_baselines3 import DQN
import torch
import matplotlib.pyplot as plt
import numpy as np

# Check if MPS is available (for Mac M1 devices), otherwise fallback to CPU
device = 'mps' if torch.backends.mps.is_available() else 'cpu'
print(f"Using device: {device}")

# URL for the BOPTEST service.
url = 'http://localhost:5001/' 

# Modify the environment to simulate for two weeks (14 days)
env = BoptestGymEnv(
    url                  = url,
    actions              = ['oveHeaPumY_u'],
    observations         = {'time':(0,604800),
                            'reaTZon_y':(280.,310.),
                            'TDryBul':(265,303),
                            'HDirNor':(0,862),
                            'InternalGainsRad[1]':(0,219),
                            'PriceElectricPowerHighlyDynamic':(-0.4,0.4),
                            'LowerSetp[1]':(280.,310.),
                            'UpperSetp[1]':(280.,310.)},
    predictive_period    = 24 * 3600,  # Predict over two weeks
    regressive_period    = 6 * 3600, 
    max_episode_length   = 7 * 24 * 3600,  # Simulate for 14 days
    warmup_period        = 24 * 3600,  # 1-day warmup
    step_period          = 3600  # 1-hour steps
)

# Normalize observations and discretize action space (if required)
env = NormalizedObservationWrapper(env)
env = DiscretizedActionWrapper(env, n_bins_act=10)

# Assuming the model is already trained and in memory
# You can instantiate the model again here if necessary
# If the model was saved, you could also load it like this:
model = DQN.load("/Users/hanskrio/Desktop/NTNU/Prosjektoppgave/code/RL_energy/checkpoint_dqn_model_test_10_steps.zip", env=env)

# Loop for one episode of experience (two weeks)
done = False
obs, _ = env.reset()
while not done:
    action, _ = model.predict(obs, deterministic=True)  # Use the trained model to predict actions
    obs, reward, terminated, truncated, info = env.step(action)
    done = (terminated or truncated)

# Obtain KPIs after two weeks
kpis = env.get_kpis()
print("Evaluation KPIs:")
for key, value in kpis.items():
    print(f"{key}: {value}")