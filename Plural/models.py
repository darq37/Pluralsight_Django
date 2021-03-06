from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse

# Create your models here.
GAME_STATUS_CHOICES = (
    ('F', "First Player To Move"),
    ('S', "Second Player To Move"),
    ('W', "First Player Wins"),
    ('L', "Second Player Wins"),
    ('D', "Draw"),
)
BOARD_SIZE = 3

class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
        )


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.CASCADE)

    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    objects = GamesQuerySet.as_manager()

    def new_move(self):
        if self.status not in 'FS':
            raise ValueError("Cannot make move on finished game")
        return Move(
            game=self,
            by_first_player=self.status == 'F'
        )

    def is_users_move(self, user):
        return (user==self.first_player and self.status=='F') or (user ==self.second_player and self.status=='S')

    def board(self):
        board =[[None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.y][move.x] = move
        return board

    def get_abs_url(self):
        return reverse('gameplay_detail', args=[self.id])

    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player
        )


class Move(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE -1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(BOARD_SIZE -1)])
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField(editable=False)

    game = models.ForeignKey(Game, on_delete=models.CASCADE, editable=False)
