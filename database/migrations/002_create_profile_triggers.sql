BEGIN;

-- 1. Automatically create a profile for new users

CREATE FUNCTION public.handle_new_user()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = ''
AS $$
BEGIN

    INSERT INTO public.profiles (
        id,
        full_name,
        role
    )
    VALUES (
        NEW.id,
        LEFT(
            NEW.raw_user_meta_data ->> 'full_name',
            150
        ),
        'customer'
    );

    RETURN NEW;

END;
$$;


-- 2. Register the authentication trigger

CREATE TRIGGER on_auth_user_created
AFTER INSERT ON auth.users
FOR EACH ROW
EXECUTE FUNCTION public.handle_new_user();


-- 3. Automatically update the updated_at timestamp

CREATE FUNCTION public.handle_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
SET search_path = ''
AS $$
BEGIN

    NEW.updated_at = NOW();

    RETURN NEW;

END;
$$;


-- 4. Register the profile update trigger

CREATE TRIGGER on_profile_updated
BEFORE UPDATE ON public.profiles
FOR EACH ROW
EXECUTE FUNCTION public.handle_updated_at();


-- 5. Restrict direct function execution

REVOKE EXECUTE
ON FUNCTION public.handle_new_user()
FROM PUBLIC, anon, authenticated;

REVOKE EXECUTE
ON FUNCTION public.handle_updated_at()
FROM PUBLIC, anon, authenticated;

COMMIT;    