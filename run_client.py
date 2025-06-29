from whisper_live.client import TranscriptionClient
client = TranscriptionClient(
  "195.0.159.206",
  43796,
  lang="en",
  translate=False,
  model="small",                                      # also support hf_model => `Systran/faster-whisper-small`
  use_vad=False,
  save_output_recording=True,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav", # Only used for microphone input
  max_clients=4,
  max_connection_time=600,
  mute_audio_playback=False,                          # Only used for file input, False by Default
)
client()