package com.project.bolcso.Service;

import boofcv.io.webcamcapture.UtilWebcamCapture;
import com.github.sarxos.webcam.Webcam;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import javax.imageio.ImageIO;
import javax.xml.bind.DatatypeConverter;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Objects;

@Slf4j
@Service
public class StreamService {

    @Autowired
    private SimpMessagingTemplate simpMessagingTemplate;

    private Webcam webcam = null;

//    @Scheduled(fixedDelay = 16)
    private void capture() {
        try {
            if (Objects.isNull(webcam)) {
                webcam = UtilWebcamCapture.openDefault(1080, 720);
                log.info("Video stream is live now");
            }
            if (webcam.isOpen()) {
                BufferedImage image = webcam.getImage();
                if (Objects.nonNull(image)) {
                    ByteArrayOutputStream baos = new ByteArrayOutputStream();
                    ImageIO.write(image, "jpeg", baos);
                    simpMessagingTemplate.convertAndSend("/topic/messages", "data:image/png;base64," + DatatypeConverter.printBase64Binary(baos.toByteArray()));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
