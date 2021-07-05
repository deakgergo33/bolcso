package com.project.bolcso.controller;

import boofcv.io.webcamcapture.UtilWebcamCapture;
import com.github.sarxos.webcam.Webcam;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.awt.image.BufferedImage;

@Controller
@RequestMapping(value = "/stream")
public class StreamController {

    private boolean isStreaming = false;

    @RequestMapping(method = RequestMethod.GET, value="/start")
    @ResponseBody
    public void start() {
        if (!isStreaming) {
            isStreaming = true;
            Webcam webcam = UtilWebcamCapture.openDefault(640, 480);
            while (isStreaming) {
                BufferedImage image = webcam.getImage();
                //TODO: send to client
            }
            webcam.close();
        }
    }

    @RequestMapping(method = RequestMethod.GET, value="/stop")
    @ResponseBody
    public void stop() {
        isStreaming = false;
    }
}
