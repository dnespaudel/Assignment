import os
import uuid


def generate_filename(filename, keyword):
    """
    Generate filename with uuid and a keyword
    :param filename: original filename
    :param keyword: keyword to be attached with uuid
    :return: string of new path
    """
    ext = filename.split('.')[-1]
    new_filename = '{}_{}.{}' .format(keyword, uuid.uuid4, ext)
    return new_filename


def upload_to_folder(instance, filename, folder, keyword):
    """

    :param instance: model instance
    :param filename: original filename
    :param folder: folder name where it should be stored
    :param keyword: keyword to be attached with uuid
    :return: string of new path
    """
    return os.path.join(
        folder,
        generate_filename(
            filename=filename,
            keyword=keyword,
        ))


def mail_image_to(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return '{}.{}'.format(instance.pk, ext)
