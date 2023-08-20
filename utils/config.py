import os

from dotenv.main import load_dotenv

from .logging import logger


class Config:
    def __init__(self):
        load_dotenv()

        self.guild_id = int(os.environ.get("MAIN_GUILD_ID"))

        if self.guild_id is None:
            self.setup_error("MAIN_GUILD_ID")
        logger.info(
            f"GIR will be running in: {self.guild_id}")

    def setup_warning(self, k: str):
        logger.warn(
            '.env file does not have key {}. Some features may not function as intended.'.format(k))

    def setup_error(self, k: str):
        logger.error(
            '.env file is not correctly set up! Missing key {}'.format(k))
        exit(1)


cfg = Config()
