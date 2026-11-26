BEGIN;

-- Create user role enum
CREATE TYPE public.user_role AS ENUM (
    'customer',
    'mechanic',
    'admin'
);

-- Create application profiles table
CREATE TABLE public.profiles (

    id UUID PRIMARY KEY
        REFERENCES auth.users(id)
        ON DELETE CASCADE,

    full_name VARCHAR(150),

    phone VARCHAR(20),

    avatar_url TEXT,

    role public.user_role
        NOT NULL DEFAULT 'customer',

    is_active BOOLEAN
        NOT NULL DEFAULT TRUE,

    created_at TIMESTAMPTZ
        NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMPTZ
        NOT NULL DEFAULT NOW()

);

-- Create index
CREATE INDEX idx_profiles_role
ON public.profiles(role);

-- Enable Row Level Security
ALTER TABLE public.profiles
ENABLE ROW LEVEL SECURITY;

-- Restrict direct client permissions
REVOKE ALL ON public.profiles
FROM PUBLIC, anon, authenticated;

-- Allow authenticated users to read profiles
GRANT SELECT ON public.profiles
TO authenticated;

-- Allow users to update only safe columns
GRANT UPDATE (full_name, phone, avatar_url)
ON public.profiles
TO authenticated;

-- Users can read their own profile
CREATE POLICY profiles_select_own
ON public.profiles
FOR SELECT
TO authenticated
USING (auth.uid() = id);

-- Active users can update their own profile
CREATE POLICY profiles_update_own
ON public.profiles
FOR UPDATE
TO authenticated
USING (auth.uid() = id AND is_active)
WITH CHECK (auth.uid() = id AND is_active);

COMMIT;