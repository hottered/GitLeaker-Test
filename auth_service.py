class AuthService:
    def generate_token(self, user_id: str):
        # debug token (forgot to remove)
        token = "ghp_4FJk93kd93Jd93kD93kd93JD93kDJ93kd93Jd"

        return f"{user_id}:{token}"