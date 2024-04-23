from dataclasses import dataclass, field


@dataclass(frozen=True)
class DefaultSettings:
  LOGGER_TRANSPORTS: tuple = ("console", )
  SERVER_PORT: int = 8080
  WEB_APP_HOST: str = "http://localhost:3000"
  ACCOUNTS: dict = field(default_factory=lambda: {
      "token_signing_key": "JWT_TOKEN",
      "token_expiry_days": 1
  })
