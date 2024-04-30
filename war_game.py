import pydealer


class Player:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def main():
    first_player, second_player = get_players_names()
    first_player_cards, second_player_cards = prepare_cards()
    first_player_stash, second_player_stash = play_game(first_player, second_player, first_player_cards, second_player_cards)
    if first_player_stash > second_player_stash:
        print(f"Player {first_player} WON!")
    else:
        print(f"Player {second_player} WON!")
    
    


def get_players_names():
    first_player = input("First Player: ").title().strip()
    second_player = input("Second Player: ").title().strip()
    return first_player, second_player


def prepare_cards():
    deck = pydealer.Deck(rebuild=True, re_shuffle=True)
    deck.shuffle()
    first_player_cards = list(deck.deal(26))
    second_player_cards = list(deck.deal(26))
    return first_player_cards, second_player_cards


def play_game(
    first_player: Player, second_player: Player, first_player_cards, second_player_cards
):
    first_player_stash = []
    second_player_stash = []
    round = 1

    while first_player_cards and second_player_cards:
        first_player_card = first_player_cards.pop()
        second_player_card = second_player_cards.pop()

        next_round = input("Next?: ").strip().lower()
        if next_round == "yes":
            if first_player_card.value > second_player_card.value:
                first_player_stash.extend([first_player_card, second_player_card])
                print(
                    f"--------------------\nRound {round}:\n{first_player} card '{first_player_card}' is higher than {second_player} card '{second_player_card}'"
                )

            elif first_player_card.value < second_player_card.value:
                second_player_stash.extend([first_player_card, second_player_card])
                print(
                    f"--------------------\nRound {round}:\n{second_player} card '{second_player_card}' is higher than {first_player} card '{first_player_card}'"
                )

            elif (
                first_player_card.value == second_player_card.value
                and len(first_player_cards) > 1
                and len(second_player_cards) > 1
            ):
                print(
                    f"WAR!\nRound {round}:\n{first_player} card '{first_player_card}' is equal to {second_player} card '{second_player_card}'"
                )
                (
                    first_player_stash,
                    second_player_stash,
                    first_player_cards,
                    second_player_cards,
                ) = play_war(
                    first_player,
                    second_player,
                    first_player_card,
                    second_player_card,
                    first_player_stash,
                    second_player_stash,
                    first_player_cards,
                    second_player_cards,
                )

            else:
                break
            round += 1

            print(
                f"Result:\n{first_player} has {len(first_player_cards)} cards and {len(first_player_stash)} in stash\n{second_player} has {len(second_player_cards)} cards and {len(second_player_stash)} in stash\n"
            )
            
        else:
            print("Enter YES to proceed")
            continue
    
    return first_player_stash, second_player_stash


def play_war(
    first_player,
    second_player,
    first_player_card,
    second_player_card,
    first_player_stash,
    second_player_stash,
    first_player_cards,
    second_player_cards,
):
    war_stash = []
    war_stash.extend([first_player_card, second_player_card])

    while first_player_cards and second_player_cards:
        first_player_card = first_player_cards.pop()
        second_player_card = second_player_cards.pop()
        next_round = input("Next?: ").strip().lower()
        if next_round == "yes":
            if first_player_card.value > second_player_card.value:
                war_stash.extend([first_player_card, second_player_card])
                first_player_stash.extend(war_stash)
                print(
                    f"{first_player} card '{first_player_card}' is higher than {second_player} card '{second_player_card}'\n-------------------\n{first_player} won WAR\n-------------------"
                )
                return (
                    first_player_stash,
                    second_player_stash,
                    first_player_cards,
                    second_player_cards,
                )

            elif first_player_card.value < second_player_card.value:
                war_stash.extend([first_player_card, second_player_card])
                second_player_stash.extend(war_stash)
                print(
                    f"{second_player} card '{second_player_card}' is higher than {first_player} card '{first_player_card}'\n-------------------\n{second_player} won WAR\n-------------------"
                )
                return (
                    first_player_stash,
                    second_player_stash,
                    first_player_cards,
                    second_player_cards,
                )

            elif (
                first_player_card.value == second_player_card.value
                and len(first_player_cards) > 1
                and len(second_player_cards) > 1
            ):
                print("WAR CONTINUES!")
                continue

            else:
                break
        else:
            continue


if __name__ == "__main__":
    main()
