from beets.plugins import BeetsPlugin
import musicbrainzngs
import re
import mediafile

class MoodsWriterPlugin(BeetsPlugin):
  def __init__(self):
    super(MoodsWriterPlugin, self).__init__()
    
    self.mood = None
    
    self.template_fields['mood'] = self._tmpl_mood

    field = mediafile.MediaField(
        mediafile.MP3StorageStyle("TMOO"), 
        mediafile.MP3StorageStyle("TXXX:MOOD"), 
        mediafile.MP4StorageStyle("----:com.apple.iTunes:MOOD"),
        mediafile.StorageStyle("MOOD"),
        mediafile.ASFStorageStyle("WM/Mood"),
    )
    self.add_media_field("mood", field)

  def _tmpl_mood(self, item):
    mood = "unknown"
    factor = 0.0 
    min_mood = 0.5

    if item['mood_acoustic'] is not None and item['mood_acoustic'] > min_mood:
        mood = "acoustic"
        factor = item['mood_acoustic']

    if item['mood_aggressive'] is not None and item['mood_aggressive'] > min_mood and item['mood_aggressive'] > factor:
        mood = "aggressive"
        factor = item['mood_aggressive']

    if item['mood_electronic'] is not None and item['mood_electronic'] > min_mood and item['mood_electronic'] > factor:
        mood = "electronic"
        factor = item['mood_electronic']

    if item['mood_happy'] is not None and item['mood_happy'] > min_mood and item['mood_happy'] > factor:
        mood = "happy"
        factor = item['mood_happy']

    if item['mood_party'] is not None and item['mood_party'] > min_mood and item['mood_party'] > factor:
        mood = "party"
        factor = item['mood_party']

    if item['mood_relaxed'] is not None and item['mood_relaxed'] > min_mood and item['mood_relaxed'] > factor:
        mood = "relaxed"
        factor = item['mood_relaxed']

    if item['mood_sad'] is not None and item['mood_sad'] > min_mood and item['mood_sad'] > factor:
        mood = "sad"

    return mood

