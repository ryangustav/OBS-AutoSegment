import obspython as obs
import threading
import time
import os
import platform

recording_interval = 1800  
stop_flag = False
thread = None
is_running = False
start_stop_button = None
videos_gravados = 0

def script_description():
    return "Salva e reinicia a gravação automaticamente a cada X minutos. Inclui contador e atalho para a pasta de gravação."

def script_properties():
    global start_stop_button
    props = obs.obs_properties_create()

    obs.obs_properties_add_int(props, "interval", "Intervalo (minutos)", 1, 180, 1)
    start_stop_button = obs.obs_properties_add_button(props, "start_stop_button", "Loop Start/Stop", toggle_loop)

    return props

def script_update(settings):
    global recording_interval
    interval = obs.obs_data_get_int(settings, "interval")
    recording_interval = interval * 60

def script_load(settings):
    log_info("Script carregado.")

def script_unload():
    global stop_flag
    stop_flag = True
    log_info("Script descarregado.")

def toggle_loop(props, prop):
    global is_running
    if not is_running:
        start_loop()
    else:
        stop_loop()

def start_loop():
    global stop_flag, thread, is_running, start_stop_button, videos_gravados
    if thread and thread.is_alive():
        return
    stop_flag = False
    is_running = True
    videos_gravados = 0
    thread = threading.Thread(target=recording_loop)
    thread.start()
    if start_stop_button:
        obs.obs_property_set_description(start_stop_button, "Parar Loop")
    log_info("Loop de gravação iniciado.")

def stop_loop():
    global stop_flag, is_running, start_stop_button
    stop_flag = True
    is_running = False
    if start_stop_button:
        obs.obs_property_set_description(start_stop_button, "Iniciar Loop")
    log_info("Loop de gravação parado.")

def recording_loop():
    global stop_flag, videos_gravados
    while not stop_flag:
        if not obs.obs_frontend_recording_active():
            log_info("Iniciando gravação...")
            obs.obs_frontend_recording_start()
        else:
            log_info("Gravação já estava ativa.")

        tempo = 0
        while tempo < recording_interval and not stop_flag:
            time.sleep(1)
            tempo += 1

        if obs.obs_frontend_recording_active():
            log_info("Parando gravação...")
            obs.obs_frontend_recording_stop()
            videos_gravados += 1
            log_estado()

        if stop_flag:
            break
        time.sleep(2)


def log_info(msg):
    obs.script_log(obs.LOG_INFO, f"[AutoRec] {msg}")

def log_estado():
    log_info(f"Estado atual: {'Gravando' if obs.obs_frontend_recording_active() else 'Parado'}")
    log_info(f"Vídeos gravados nesta sessão: {videos_gravados}")
