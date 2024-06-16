# Damaged-Lane-Marking-Classification
차선 훼손 분류 프로젝트

Label
![스크린샷 2024-06-16 194719](https://github.com/Jangorithm/Damaged-Lane-Marking-Classification/assets/92138169/e23f9cd5-3a8e-4d4e-9a3c-df69cd83c5f4)

도로 (Road) - 0

훼손된 차선 영역 (Damaged lane area) - 1

정상 차선 영역 (Normal lane area) - 2


24.06.16 Segmentation을 활용한 차선 훼손 v1.ipynb 
- 도로 배경을 제외 후 차선 이미지만 다중 분류 Segmentation할 경우 훼손된 차선의 영역을 잘 예측을 함
(When performing multi-class segmentation of lane markings excluding the road background, the model predicts the damaged lane areas accurately.)
- 하지만, 도로 배경을 포함한 상태에서의 훼손된 차선의 영역을 잘 예측하지 못함
(However, it struggles to predict damaged lane areas well when including the road background.)
- 도로 영역 과 훼손된 차선 영역의 특징이 비슷하기에 보완 방법이 필요함
(This is because the features of the road area and the damaged lane area are similar, necessitating the need for supplementary methods.)



