package com.project.bolcso.controller;

import com.project.bolcso.Service.StreamService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/stream")
public class StreamController {

    @Autowired
    private StreamService streamService;

    @RequestMapping()
    protected ModelAndView view() {
        streamService.capture();
        return new ModelAndView("temp");
    }
}
