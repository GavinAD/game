WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0

time_left = 10

q1 = ["When was the current flag of the United States adopted?",
    "1773", "1775", "1625", "1960", 4]

q2 = ["Which of these flags is an atypical shape?",
    "Nepal", "China", "Mali", "Equador", 1]

q3 = ["Which of these flags uses the pan-slavic colors?",
    "Germany", "Poland", "Czechia", "Japan", 3]

q4 = ["Which flag features the most colors?",
    "Russia", "Barbados", "Ghana", "Eswanti", 4]

q5 = ["What is the oldest national flag still in use?", 
    "China", "Denmark", "Morocco", "UK", 2]
    
q6 = ["Which of these flags uses the Nordic Cross?"
    "Greenland", "Iceland", "England", "Germany", 2]
    
q7 = ["Which country's flag inspired a set of Pan-African colors?"
    "Ethiopia", "Mali", "South Africa", "Egypt", 1]
    
q8 = ["What colors are on the flag of Angola?"
    "Black, Green, Red", "Blue, Red, White", "Black, Blue, Yellow", "Black, Red, Yellow", 4]

questions = [q1, q2, q3, q4, q5, q6, q7, q8]
question = questions.pop(0)

def draw():
    screen.fill("dark red")
    screen.draw.filled_rect(main_box, "indigo")
    screen.draw.filled_rect(timer_box, "indigo")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "purple")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1

def game_over():
    global question, time_left
    message = "Game Over, You Got %s Questions Correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left
    
    score = score + 1
    if questions:
            question = questions.pop(0)
            time_left = 10
    else:
        print("End of Questions")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on Answer " + str(index))
            if index == question[5]:
                print("You Got It Correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1

def update_timer_left():
    global time_left
    
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

