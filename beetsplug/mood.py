from beets.plugins import BeetsPlugin
import mediafile

class MoodPlugin(BeetsPlugin):
  def __init__(self):
    super(MoodPlugin, self).__init__()
    
    field = mediafile.MediaField(
        mediafile.MP3StorageStyle("TMOO"), 
        mediafile.MP3StorageStyle("TXXX:MOOD"), 
        mediafile.MP4StorageStyle("----:com.apple.iTunes:MOOD"),
        mediafile.StorageStyle("MOOD"),
        mediafile.ASFStorageStyle("WM/Mood"),
    )
    self.add_media_field("mood", field)
