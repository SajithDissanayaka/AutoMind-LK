from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.profile import Profile
from app.schemas.profile import ProfileResponse


def test_profile_model():

    with SessionLocal() as db:

        statement = select(Profile).limit(5)

        profiles = db.scalars(statement).all()

        print("Database query successful")
        print(f"Profiles found: {len(profiles)}")

        for profile in profiles:

            response = ProfileResponse.model_validate(
                profile
            )

            print("-" * 40)

            print(response.model_dump_json(indent=4))


if __name__ == "__main__":

    test_profile_model()