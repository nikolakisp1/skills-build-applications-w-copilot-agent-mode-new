from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Verify the test data in the database'

    def handle(self, *args, **kwargs):
        # Verify Users
        users = User.objects.all()
        self.stdout.write(f"Users: {users}")

        # Verify Teams
        teams = Team.objects.all()
        self.stdout.write(f"Teams: {teams}")

        # Verify Activities
        activities = Activity.objects.all()
        self.stdout.write(f"Activities: {activities}")

        # Verify Leaderboard
        leaderboard = Leaderboard.objects.all()
        self.stdout.write(f"Leaderboard: {leaderboard}")

        # Verify Workouts
        workouts = Workout.objects.all()
        self.stdout.write(f"Workouts: {workouts}")