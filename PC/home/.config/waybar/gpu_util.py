def get_gpu_and_mem_busy_percent():
    """
    Liest die GPU- und Speicher-Auslastung von den angegebenen Pfaden aus und gibt sie als Prozentwerte zurück.
    Returns:
        tuple: Ein Tupel, bestehend aus (gpu_busy_percent, mem_busy_percent, vram_percent, vram_used).
               Gibt (None, None) zurück, wenn ein Fehler beim Lesen der Dateien auftritt.
    """
    try:
        with open("/sys/class/drm/card0/device/gpu_busy_percent", "r") as f_gpu:
            gpu_busy_percent = f_gpu.read().strip()
            gpu_busy_percent = gpu_busy_percent + "%"

        with open("/sys/class/drm/card0/device/mem_busy_percent", "r") as f_mem:
            mem_busy_percent = f_mem.read().strip()
            mem_busy_percent = mem_busy_percent + "%"

        with open("/sys/class/drm/card0/device/mem_info_vram_used", "r") as v_use:    
            vram_used = v_use.read().strip()
            vram_used_gb = float(vram_used) / 1024 / 1024 / 1024
            vram_used_gb = str(round(vram_used_gb, 2)) + "Gi"

        return (gpu_busy_percent, mem_busy_percent, vram_used_gb)

    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        return (None, None, None)

gpu_busy, mem_busy, vram_used = get_gpu_and_mem_busy_percent()
if gpu_busy is not None and mem_busy is not None:
    print(f"{gpu_busy} | {mem_busy} | {vram_used}")