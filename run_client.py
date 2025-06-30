from whisper_live.client import TranscriptionClient
client = TranscriptionClient(
  "213.181.122.2",
  40855,
  lang="fa",
  translate=False,
  model="large-v3",                                      # also support hf_model => `Systran/faster-whisper-small`
  use_vad=False,
  save_output_recording=True,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav", # Only used for microphone input
  max_clients=4,
  max_connection_time=6000,
  mute_audio_playback=False,                          # Only used for file input, False by Default
)
client("test_files/src-48065 dst-10100 channel-SIP_Grandstream dstchannel-SIP_106 3-08-22 08_33.wav")