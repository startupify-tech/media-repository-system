import uuid
import datetime


def get_file_path(instance, filename):

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    now = datetime.datetime.now().strftime('%y/%m')
    if instance.Author.id is not None:
        return 'media/{0}/{1}/{2}'.format(now, instance.Author.username, filename)