from streamlit_webrtc import webrtc_streamer
import av
import cv2


class VideoProcessor:
  def recv(self, frame):
    frm = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(frm, format='bgr24')

webrtc_streamer(key="sample" , 
                rtc_configuration= {
                    "iceServers" : [{"urls":["stun:stun1.l.google.com:19302"]}]
                },
                video_processor_factory=VideoProcessor
                )
