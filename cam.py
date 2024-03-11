import cv2

# 웹캠 설정
cap = cv2.VideoCapture(0)

while True:
    # 비디오의 현재 프레임을 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽혔는지 확인
    if not ret:
        break

    # 프레임을 화면에 표시
    cv2.imshow('Press Space to Capture', frame)

    # 사용자가 키를 누를 때까지 대기
    key = cv2.waitKey(1)

    # 스페이스바를 누르면 현재 화면을 파일로 저장
    if key == 32:  # 스페이스바 ASCII 코드
        cv2.imwrite('photo.jpg', frame)
        print("Photo captured and saved!")

    # 'q'를 누르면 루프에서 빠져나옴
    if key == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
