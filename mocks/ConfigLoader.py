from InsightUtilities.ConfigLoader import ConfigLoader
import os

class ConfigLoader(ConfigLoader):
    def _load_all_options(self):
        self.parse_str("CCP_CLIENT_ID", "ccp_developer", "client_id", False, os.environ.get("sso_client_id"), True)
        self.parse_str("CCP_SECRET_KEY", "ccp_developer", "client_id", False, os.environ.get("sso_secret_key"), True)
        self.parse_str("CCP_CALLBACK_URL", "ccp_developer", "client_id", False, os.environ.get("sso_callback_url"), True)
        self.parse_str("DISCORD_TOKEN", "discord", "token", False, "UnitTestingTokenBlank", True)
        self.parse_int("LIMITER_GLOBAL_SUSTAIN_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GLOBAL_SUSTAIN_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GLOBAL_BURST_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GLOBAL_BURST_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_DM_SUSTAIN_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_DM_SUSTAIN_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_DM_BURST_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_DM_BURST_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GUILD_SUSTAIN_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GUILD_SUSTAIN_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GUILD_BURST_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_GUILD_BURST_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_CHANNEL_SUSTAIN_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_CHANNEL_SUSTAIN_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_CHANNEL_BURST_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_CHANNEL_BURST_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_USER_SUSTAIN_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_USER_SUSTAIN_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_USER_BURST_TICKETS", "NULL", "NULL", False, 500, True)
        self.parse_int("LIMITER_USER_BURST_INTERVAL", "NULL", "NULL", False, 500, True)
        self.parse_str("ZK_REDISQ_URL", "NULL", "NULL", False, "https://redisq.zkillboard.com/listen.php", True)
        self.parse_str("ZK_WS_URL", "NULL", "NULL", False, "wss://zkillboard.com/websocket/", True)
        self.parse_bool("WEBSERVER_ENABLED", "NULL", "NULL", False, "FALSE", True)
        self.parse_bool("ZK_ID_RESET", "NULL", "NULL", False, "FALSE", True)