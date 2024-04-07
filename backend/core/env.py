import environ
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cast values and assign 
env = environ.Env(
    # Debugging
    DEBUG       = (bool, True),
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env.local'))
