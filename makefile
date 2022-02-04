deploy:
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe Expand-Archive matlab/crypto_images.zip matlab
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe Expand-Archive matlab/models/iaprtc12.zip matlab/models
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe Expand-Archive matlab/images/_images_from_kiran.zip matlab/images

clean:
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe Compress-Archive -CompressionLevel "NoCompression" matlab/crypto_images -Update matlab/crypto_images.zip
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe rm -r matlab/crypto_images
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe rm -r matlab/models/iaprtc12
	C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe rm -r matlab/images/_images_from_kiran

test:
	python -m mypy salsa
	python -m mypy tests

	python -m flake8 salsa
	python -m flake8 tests

	python -m pytest tests --durations=5
