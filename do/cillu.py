def runtime_lavamoat_cache_editor(cache_path, is_enable):
    """
    Enable or disable the runtime lavamoat cache.
    Args:
        cache_path (str): Path to the cache file.
        is_enable (bool): True to enable, False to disable.
    """
    cache_file = open(cache_path, "w")
    cache_file.write(str(is_enable))
    cache_file.close()  
