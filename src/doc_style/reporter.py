from .profile import resolve_profile, apply_profile


def run():
    p = resolve_profile()
    return apply_profile(p)
