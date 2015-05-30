(require 'uniquify)
(setq uniquify-buffer-name-style 'reverse)

;; prevent silly initial splash screen
(setq inhibit-splash-screen t)

(setq-default indent-tabs-mode nil)

(add-hook 'before-save-hook 'delete-trailing-whitespace)

;; swugklpywfmmbuxi
;; sudo killall -v -c nxserver.bin -SIGKILL