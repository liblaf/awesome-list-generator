import pydantic

from . import Category, Configuration, ProjectConfig


class Config(pydantic.BaseModel):
    config: Configuration = pydantic.Field(default_factory=Configuration)
    categories: list[Category] = []
    projects: list[ProjectConfig] = []
