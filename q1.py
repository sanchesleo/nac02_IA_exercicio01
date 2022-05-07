#RM82064
import cv2

cap = cv2.VideoCapture("q1.mp4")
card_cascade_spade = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Seu código aqui. 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cards_spade = card_cascade_spade.detectMultiScale(gray,1.2,5,0,(50,50))
    for (x,y,w,h) in cards_spade:
        cv2.putText(frame, 'Carta encontrada', ((x-50,y-50)), cv2.FONT_HERSHEY_SIMPLEX, 1, (124,252,0), 2, cv2.LINE_AA)

        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(124,252,0),2)
        frameS = cv2.resize(frame, (1000, 600))

        # Exibe resultado
        cv2.imshow("Feed", frameS)

        # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()