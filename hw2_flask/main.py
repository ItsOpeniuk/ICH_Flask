from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator # 'ection=after'


class Address(BaseModel):

    city: str = Field(..., min_length=2, max_length=30)
    street: str = Field(..., min_length=3, max_length=30)
    house_number: int = Field(..., gt=0)


class User(BaseModel):

    name: str = Field(..., min_length=3, max_length=20)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr
    is_employer: bool = Field(...)
    address: Address

    @field_validator("name")
    def validate_name(cls, value: str):

        if not value.isalpha():
            raise ValueError("Name should be the letters only")

        return value

    @model_validator(mode='after')
    def validate_employment_opportunity(self):

        if self.age < 18 and self.is_employer:
            raise ValueError("You`r can`t be employed because your age is less than 18")

        return self


def main(data: str):
    try:
        user = User.model_validate_json(data)
        return user.model_dump_json()
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    user_data = """
    {
        "name": "Yevhen",
        "age": 34,
        "email": "openyusha@gmail.com",
        "is_employer": true,
        "address": {
            "city": "Mariupol",
            "street": "Pobedy",
            "house_number": 131
        }
    }
    """
    print(main(data=user_data))
