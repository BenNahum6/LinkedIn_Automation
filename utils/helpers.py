from utils.logger import logger
import re

def extract_number_from_invitations_text(text):
    """
    Extracts the number of pending invitations from a text like "Invitations (3)".

    :param text: Text to parse (e.g., "Invitations (3)").
    :return: Number of invitations (int), or 0 if parsing fails.
    """
    try:
        match = re.search(r'\((\d+)\)', text)
        return int(match.group(1))
    except (IndexError, ValueError):
        logger.error(f"Failed to extract number from text: {text}")
        return 0