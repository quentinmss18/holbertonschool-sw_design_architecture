#!/usr/bin/env python3
"""Observer pattern - news notification system."""


class NewsSubject:
    """Subject that publishes news events to registered observers."""

    def __init__(self):
        """Initialize with an empty subscriber list."""
        self._subscribers = {}

    def subscribe(self, observer, topics=None) -> None:
        """Register an observer for given topics.

        Args:
            observer: the observer object to register.
            topics: a set of topic strings, or None to receive all topics.
        """
        self._subscribers[observer] = topics

    def unsubscribe(self, observer) -> None:
        """Remove an observer from the subscriber list.

        Args:
            observer: the observer to remove.
        """
        self._subscribers.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        """Notify all relevant observers of a new event.

        Args:
            topic: the topic of the event.
            data: the event data payload.
        """
        snapshot = list(self._subscribers.items())
        for observer, topics in snapshot:
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs events to stdout."""

    def update(self, topic: str, data: str) -> None:
        """Handle a notification event.

        Args:
            topic: the topic of the event.
            data: the event data payload.
        """
        print("log:{}={}".format(topic, data))


class EmailObserver:
    """Observer that sends email notifications."""

    def update(self, topic: str, data: str) -> None:
        """Handle a notification event.

        Args:
            topic: the topic of the event.
            data: the event data payload.
        """
        print("email:{}={}".format(topic, data))


class SmsObserver:
    """Observer that sends SMS notifications."""

    def update(self, topic: str, data: str) -> None:
        """Handle a notification event.

        Args:
            topic: the topic of the event.
            data: the event data payload.
        """
        print("sms:{}={}".format(topic, data))


def main():
    """Demonstrate the observer notification system."""
    subject = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    subject.subscribe(log_obs, topics={"sports", "breaking"})
    subject.subscribe(email_obs)
    subject.subscribe(sms_obs, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
