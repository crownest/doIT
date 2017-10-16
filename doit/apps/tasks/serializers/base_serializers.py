# Third-Party
from rest_framework import serializers

# Local Django
from tasks.models import Task, Reminder


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderListSerializer(ReminderSerializer):
    pass


class ReminderCreateSerializer(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('task', 'date')


class ReminderRetrieveSerializer(ReminderSerializer):
    pass


class ReminderUpdateSerializer(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('date',)


class TaskSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskListSerializer(TaskSerializer):

    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskCreateSerializer(TaskSerializer):
    reminders = ReminderCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'reminders')


class TaskRetrieveSerializer(TaskSerializer):
    reminders = ReminderRetrieveSerializer(many=True, read_only=True)


class TaskUpdateSerializer(TaskSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description')