<?php

namespace jorgebg\cv;

require 'vendor/autoload.php';

use Symfony\Component\Yaml\Yaml;
use cebe\markdown\latex\Markdown;
use ArrayObject;

class Generator {
  public $texTemplate = 'tml/cv.tex.php';
  public $texFile = 'tex/cv.tex';
  public $cvFile = 'cv.yaml';
  public $privateCvFile = 'cv.private.yaml';

  public function run() {
    $data = $this->loadData();
    $tex = $this->render($data);
    file_put_contents($this->texFile, $tex);
  }

  protected function render($data) {
    extract((array)$data);
    ob_start();
    include $this->texTemplate;
    return ob_get_clean();
  }

  protected function loadData() {
    $data = Yaml::parse(file_get_contents($this->cvFile));
    if(file_exists($this->privateCvFile)) {
      $privateData = Yaml::parse(file_get_contents($this->privateCvFile));
      $data = array_merge($data, $privateData);
    }

    $parser = new Parser();
    array_walk_recursive($data, function(&$item, $key) use ($parser) { $item = $parser->parse($item); });
    $data = $this->toObject($data);

    return $data;
  }

  public function toObject($array) {
    $obj = new ArrayObject($array, ArrayObject::ARRAY_AS_PROPS);
    foreach ($obj as &$val) {
      $val = is_array($val) ? $this->toObject($val) : $val;
    }
    return $obj;
  }

}

class Parser extends Markdown {
  protected function renderLink($block)
  {
    if (isset($block['refkey'])) {
      if (($ref = $this->lookupReference($block['refkey'])) !== false) {
        $block = array_merge($block, $ref);
      } else {
        return $block['orig'];
      }
    }

    $url = $block['url'];
    $text = $this->renderAbsy($block['text']);
    if (strpos($url, '://') === false) {
      // consider all non absolute links as relative in the document
      // $title is ignored in this case.
      if (isset($url[0]) && $url[0] === '#') {
        $url = $this->labelPrefix . $url;
      }
      return '\hyperref['.str_replace('#', '::', $url).']{' . $text . '}';
    } else {
      return '\href{' . $this->escapeUrl($url) . '}{' . $text . '}';
    }
  }

  protected function renderParagraph($block)
  {

    return $this->renderAbsy($block['content']);
  }

}

$gen = new Generator();
$gen->run();
