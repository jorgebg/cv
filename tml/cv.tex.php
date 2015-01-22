%
% LaTeX source of my resume
% =========================
%
% Heavily commented to to fit even LaTeX beginners (hopefully).
%
% See the `README.md` file for more info.
%
% This file is licensed under the CC-NC-ND Creative Commons license.
%


% Start a document with the here given default font size and paper size.
\documentclass[10pt,a4paper]{article}

% Set the page margins.
\usepackage[a4paper,margin=0.75in]{geometry}

% Setup the language.
\usepackage[english]{babel}
\hyphenation{Some-long-word}

% Makes resume-specific commands available.
\usepackage{cv}

%Contact info table
\usepackage{array}

% Font awesome
\usepackage{fontawesome}

\begin{document}  % begin the content of the document
\sloppy  % this to relax whitespacing in favour of straight margins

% title on top of the document
\maintitle{<?=$name?>}{<?=$birthday?>}{
  \bgroup
  \def\arraystretch{1.2}
  \begin{tabular}{ m{1.5em} l }
  \faPhone & \textsmaller{+}<?=$phone?> \\
  \faEnvelopeAlt & \href{mailto:<?=$mail?>}{<?=$mail?>} \\
  \faGithub & \href{http://github.com/<?=$homepage?>}{github.com/<?=$homepage?>} \\
  \faGlobe & \href{http://<?=$homepage?>}{<?=$homepage?>} \\
  \end{tabular}
  \egroup
  }

\nobreakvspace{0.3em}  % add some page break averse vertical spacing
\noindent
<?=$address?>
\\

\spacedhrule{0.9em}{-0.4em}  % a horizontal line with some vertical spacing before and after

\roottitle{Summary}  % a root section title

\vspace{-1.3em}  % some vertical spacing
\begin{multicols}{2}  % open a multicolumn environment
\noindent \emph{<?=$intro?>}
\\
\\
<?=$description?>
\end{multicols}


\spacedhrule{0em}{-0.4em}

<? foreach(compact('experience', 'education') as $title => $section): ?>
\roottitle{<?=ucfirst($title)?>}
<? foreach($section as $sub):?>
\headedsection  % sets the header for the section and includes any subsections
  {<?=$sub->place?>}
  {\textsc{<?= $sub->location ?>}} {%
  <? foreach ($sub->items as $item): ?>
    \headedsubsection
    {<?=$item->title?>}
    {<?=$item->dates?>\smallskip}
    {
      <? foreach(is_scalar(reset($item->details)) ? [$item->details] : $item->details as $detail): ?>
      \bodytext{<?= join('\sbull ', (array)$detail) ?>\smallskip}
      <? endforeach ?>
    }
  <? endforeach ?>
}
<? endforeach ?>

<? if($section == $experience): ?>
\vspace{-0.2em}
\begin{center}
  \emph{\small Please refer to my \href{http://www.linkedin.com/in/<?= $social->linkedin ?>/en}{Linked-in profile (linkedin.com/in/<?=$social->linkedin?>/en)} to see my up to date recommendations.}
\end{center}

\spacedhrule{-0.2em}{-0.4em}
<? else: ?>
\spacedhrule{0.5em}{-0.4em}
<? endif ?>

<? endforeach ?>


<? foreach(compact('skills', 'projects', 'activities') as $title => $section): ?>
\roottitle{<?=ucfirst($title)?>}
<? foreach($section as $item): ?>
\inlineheadsection  % special section that has an inline header with a 'hanging' paragraph
{<?=$item->title?>:}
{<?= join('\sbull ', (array)$item->details) ?>}
<? endforeach ?>

\spacedhrule{1.6em}{-0.4em}
<? endforeach ?>

\vspace{1.0em}



\begin{center}
\emph{\small\color{gray} Last update on \today \ \ \ | \ \ Source code on \href{http://github.com/<?=$social->github?>/cv}{github.com/<?=$social->github?>/cv}}
\end{center}


\end{document}
