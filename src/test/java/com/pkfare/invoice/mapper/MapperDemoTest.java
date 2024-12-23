package com.pkfare.vcc.mapper;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest
@RunWith(SpringRunner.class)
@SpringBootApplication(scanBasePackages = "com.pkfare.invoice.mapper")
@MapperScan("com.pkfare.vcc.mapper")
public class MapperDemoTest {

//    @Autowired
//    private  VccCardMapper vccCardMapper;
//
//    @Test
//    public void test(){
//        VccCard vccCard = new VccCard();
//        vccCard.setCid(1);
////        Assert.(vccCardMapper.insert(vccCard)>0);;
//    }
}
