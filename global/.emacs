;; Initialize the package repos.
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(package-initialize)

;; Enable evil mode.
(require 'evil)
(evil-mode 1)

; Tab indentation with emacs is really hard to setup/find resouces on.
; The best solution I found was inserting a ASCII 9 char with the tab key
(defun my-insert-tab-char ()
  "Insert a tab char. (ASCII 9, \t)"
  (interactive)
  (insert "\t"))
(global-set-key (kbd "TAB") 'my-insert-tab-char)

;; Disable whitespace highlighting.
(setq whitespace-style (quote (face newline space-mark tab-mark newline-mark)))

;; Disable the blinking cursor.
(setq visible-cursor nil)

;; Show line numbers.
(global-linum-mode)

;; Change the line number format.
(setq linum-format "%d| ")

;; CHange the mode line format.
(setq mode-line-format (list
	"buffer %b"
))

;; Keybindings.
;; Open a file.
(define-key evil-normal-state-map "o" 'find-file)

;; Save the file.
(define-key evil-normal-state-map "s" 'evil-save)

;; Save the file and close emacs.
(define-key evil-normal-state-map "c" 'save-buffers-kill-emacs)

;; Just close emacs.
(define-key evil-normal-state-map "C" 'kill-emacs)

;; I don't know what this does.
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (evil))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
