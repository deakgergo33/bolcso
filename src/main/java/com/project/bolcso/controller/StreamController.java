package com.project.bolcso.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/stream")
public class StreamController {

    @RequestMapping()
    protected ModelAndView view() {
        return new ModelAndView("temp");
    }
}
