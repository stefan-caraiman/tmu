import pbr.version


def get_version():
    """Obtain the project version."""
    version = pbr.version.VersionInfo('tmu')
    return version.release_string()
