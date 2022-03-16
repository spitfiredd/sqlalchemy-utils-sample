from alembic_utils.pg_view import PGView


PremiumUserView = PGView(
    schema="public",
    signature="premium_users",
    definition='SELECT * FROM "user" WHERE premium_user IS TRUE'
)