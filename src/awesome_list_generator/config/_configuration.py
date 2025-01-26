import pydantic

import awesome_list_generator as alg


class Configuration(pydantic.BaseModel):
    format: alg.Format = alg.Format.MARKDOWN
