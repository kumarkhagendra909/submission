import time
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Comment
import threading
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

# Dictionary to store previous status
previous_statuses = {}

# Signal to run before saving a comment
@receiver(pre_save, sender=Comment)
def before_comment_saved(sender, instance, **kwargs):
    # Track the thread ID for proof that the signal runs in the same thread
    current_thread = threading.get_ident()
    logger.info(f"Before saving comment: {instance.name} - {instance.status} - Thread ID: {current_thread}")
    print(f"Before saving comment: {instance.name} - {instance.status} - Thread ID: {current_thread}")

    if instance.pk in previous_statuses:
        # If the instance already exists, get the previous status
        previous_status = previous_statuses[instance.pk]
    else:
        # If the instance is new, use the current status
        previous_status = instance.status

    # Store the current status before saving
    if instance.pk:
        # Update the previous status for the existing instance
        previous_statuses[instance.pk] = previous_status

    time.sleep(3) # to demonstrate 

    # Log the previous status and thread ID
    logger.info(f"Before saving comment (status): {instance.name} - {previous_status} - Thread ID: {current_thread}")
    print(f"Before saving comment (status): {instance.name} - {previous_status} - Thread ID: {current_thread}")

# Signal to run after saving a comment
@receiver(post_save, sender=Comment)
def after_comment_saved(sender, instance, created, **kwargs):
    current_thread = threading.get_ident()
    logger.info(f"After saving comment (signal): {instance.name} - Thread ID: {current_thread}")
    print(f"After saving comment (signal): {instance.name} - Thread ID: {current_thread}")

    if created:
        # For new comments
        logger.info(f"New comment saved: {instance.name} - {instance.status} - Thread ID: {current_thread}")
        print(f"New comment saved: {instance.name} - {instance.status} - Thread ID: {current_thread}")
        
    else:
        # For existing comments, print both the previous and new status
        previous_status = previous_statuses.get(instance.pk, instance.status)
        logger.info(f"Existing comment updated: {instance.name} - {previous_status} -> {instance.status} - Thread ID: {current_thread}")
        print(f"Existing comment updated: {instance.name} - {previous_status} -> {instance.status} - Thread ID: {current_thread}")
        
        # Remove the entry from previous_statuses after update
        previous_statuses.pop(instance.pk, None)

    # Demonstrating that signals run in the same transaction as the caller.

    try:
        with transaction.atomic():
            # Simulate an additional action in the transaction within the signal
            logger.info(f"Processing transaction for comment: {instance.name} - {instance.status}")
            print(f"Processing transaction for comment: {instance.name} - {instance.status}")
            # Raise an error to simulate a rollback
            if instance.status == "pending":
                print("Simulating rollback during signal processing.")
            else:
                print("Simulating commit/Saved during signal processing")
    except Exception as e:
        logger.error(f"Transaction completely failed: {str(e)}")
        print("Transaction completely failed", str(e))




