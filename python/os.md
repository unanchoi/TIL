# OS

운영체제(Operating Syetem)에서 제공되는 기능들을 종속하여 사용하는 모듈이다.

- `import os`
- `os.getcwd()` : 현재 디렉토리를 반환
- `os.listdir("경로")` : 경로에 있는
- `os.path.join("A","B")` : 2개 이상의 경로를 하나의 경로로 반환
- `os.chdir(path)`  : 디렉토리 이동
- `os.path.basedir(path)` : 해당 path에서 가장 하위 component를 반환
- `os.mkdir(dirname)` : 디렉토리 생성
- `os.environ` : 시스템의 환경변수를 사전형식으로 리턴
- `os.rmdir()` : 빈 폴더 삭제
- `os.walk(path)` : 입력한 경로로 부터, 경로 내의 모든 하우 ㅣ디렉토리까
- `os.path.exists("경로")` : 파일, 폴더이면 True, 없으면 False
- `os.path.split("경로")` : 파일명과 폴더명 분리
- `os.path.splitext("경로")` : 파일경로와 확장명 분리
- `os.path.dirname()` : 입력 경로의 폴더 경로 반환
- `os.path.basename()` :파일이름을 반환
- `os.path.isdir(path)` : path가 directory이면 True, 아니면 False 반환
- `os.path.isfile(path)` : path가 file이면 True, 아니면 False 반환
