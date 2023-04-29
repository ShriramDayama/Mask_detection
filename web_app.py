from streamlit_webrtc import webrtc_streamer
import av

def video_frame_callback(frame):
  img = frame.to_ndarray(forrmat="bgr24")
  retrun av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="sample" , 
                rtc_configuration= {
                    "iceServers" : [{"urls":["stun:stun.l.google.com:19302"]}]
                },
                video_frame_callback=video_frame_callback
                )
